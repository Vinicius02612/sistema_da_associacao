export default class EventsController {
	urlevents = "https://run.mocky.io/v3/4c9e2f42-9bd5-4a6c-8705-865ae29b912e";
	urlData = "https://run.mocky.io/v3/2d7324f9-4d73-427f-9e15-060eb33c7da9";
	urlAlerts= "https://run.mocky.io/v3/bbeb0b59-2a21-4c9e-a8dc-52d4f04c0848"

	// Método para buscar eventos
	async getEvents() {
			const response = await fetch(this.urlevents);
			if (!response.ok) {
					throw new Error(response.statusText);
			}
			const events = await response.json();
			return events;
	}

	// Método para buscar dados adicionais
	async getData() {
			const response = await fetch(this.urlData);
			if (!response.ok) {
					throw new Error(response.statusText);
			}
			const data = await response.json();
			return data;
	}

	// Remover método depois
	// Método para buscar alertas
	async getAlerts() {
		const response = await fetch(this.urlAlerts);
		if (!response.ok) {
				throw new Error(response.statusText);
		}
		const alerts = await response.json();
		return alerts;
	}
}
