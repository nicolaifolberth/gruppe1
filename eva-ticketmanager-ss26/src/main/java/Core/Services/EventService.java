package Core.Services;

import Core.Models.exceptions.EventException;
import Core.Interfaces.EventServiceInterface;
import java.time.LocalDateTime;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import Core.Models.Event;

public class EventService implements EventServiceInterface {

    private List<Event> events = new ArrayList<>();

    public Event createEvent(String name, String location, LocalDateTime time, int ticketsAvailable) throws EventException {

        UUID id = UUID.randomUUID();
        Event event = new Event(id, name, location, time, ticketsAvailable);
        events.add(new Event(id, name, location, time, ticketsAvailable));
        return event;
    }

    @Override
    public Event getEventById(UUID id) throws EventException{
        for(Event event : events) {
            if (event.getId().equals(id)){
                return event;
            }
        }
        throw EventException.eventDoesNotExist();
    }

    @Override
    public void updateEvent(Event event) throws EventException {
        Event existingDbEvent = getEventById(event.getId());
        if (event.getTime().isBefore(LocalDateTime.now())) throw EventException.cantSetEventTimeIntoPast();
        if (event.getTicketsAvailable().get() < existingDbEvent.getTicketsAvailable().get()) throw EventException.shouldNotReduceAvailableTicketsWithUpdate();
        for (Event dBevent : events) {
            if (dBevent.getId().equals(event.getId())){
                dBevent.setName(event.getName());
                dBevent.setTime(event.getTime());
                dBevent.setLocation(event.getLocation());
                dBevent.setTicketsAvailable(event.getTicketsAvailable().get());
                break;
            }
        }
    }
    // Method should check if
    private void validateUpdatedEvent(Event event) throws EventException{

        if (event.getTime().isBefore(LocalDateTime.now())) throw EventException.cantSetEventTimeIntoPast();

    }


    @Override
    public void deleteEvent(UUID id) {
        events.removeIf(e -> e.getId().equals(id));

    }

    @Override
    public List<Event> getAllEvents() {
        return events;
    }

    @Override
    public void deleteAllEvents() {
        events.clear();

    }

}

// Der Fehler besteht darin, dass event und testevent dasselbe Objekt sind.
// Dadurch führt ein Update von event direkt zu einem update von Testevent
//
