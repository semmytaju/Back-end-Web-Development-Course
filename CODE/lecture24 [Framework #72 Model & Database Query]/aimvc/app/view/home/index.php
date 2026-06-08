<div class="container">
	<h1>This is my Home Page.</h1>
	
	<p>I'm <?php echo $data['name']; ?> from Manado.</p>
	<p>I'm <?php echo $data['age']; ?> years old this year.</p>
	<p>
		<h3>Daftar Dosen:</h3>
		<?php foreach($data['lecturers'] as $lecs): ?>
			<ul>
				<li> ID: <?php echo $lecs['id']; ?> </li>
				<li> Name: <?php echo $lecs['name']; ?> </li>
				<li> E-mail: <?php echo $lecs['email']; ?> </li>
				<li> Phone: <?php echo $lecs['phone']; ?> </li>
			</ul>
		<?php endforeach; ?>
	</p>
	<img src="<?php echo APP_PATH; ?>/img/test.png" alt="test image" width="200" class="rounded-circle shadow">
</div>
